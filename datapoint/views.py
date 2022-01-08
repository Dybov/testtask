import json

from threading import Thread

from flask import jsonify, abort

from datapoint import bp
from datapoint.utils import retrieve_data, retrieve_data_thread, mergesort_lists


@bp.route('/source/<int(min=1, max=3):id>')
def get_data(id):
    """Access to sources by HTTP"""
    return jsonify(retrieve_data(id))


@bp.route('/collect-data')
def collect_data():
    """Single entrypoint that gaves correlated result"""

    # It is unclear if it should be HTTP request to all sources or just IO connection.
    # Supposed it should not be HTTP, otherwise requests lib is better to be allowed to install, but it is not by Task
    # If so, then install requests lib, uncomment 11 lines below
    # import requests
    # from flask import url_for
    # # url_for cannot be accessed out of app context, so it should be executed outside retrieve_data_thread function
    # urls = {
    #     1: url_for('datapoint.get_data', id=1, _external=True),
    #     2: url_for('datapoint.get_data', id=2, _external=True),
    #     3: url_for('datapoint.get_data', id=3, _external=True),
    # }
    # def retrieve_data_thread(id, results):
    #     """Override utils retrieve_data_thread with requests. But it will be slower"""
    #     results.append(json.loads(requests.get(urls.get(id)).content))


    def master_thread(results):
        """Makes asyncronious requests for data and gather data"""

        # this will be provided to Threads and populated with lists of data
        tmp_results = []

        threads = []
        for i in (1, 2, 3):
            thread = Thread(target=retrieve_data_thread, args=(i, tmp_results))
            # start them asynccronious
            thread.start()
            threads.append(thread)

        # wait for all responses
        for thread in threads:
            thread.join()

        # Can make it more complex
        #import time
        #time.sleep(1)

        # Merge lists in sorted order with complexity O(n+m+l)
        correlated_data = mergesort_lists(*tmp_results)

        # Keep link at results to get it outside of master_thread
        results[:] = correlated_data

    results = []
    thread = Thread(target=master_thread, args=(results,))
    thread.start()
    thread.join(2)  # Timeout for more than 2 seconds is considered as error

    if thread.is_alive():
        # It is not clear how do understand should timeout return empty dataset or an error
        abort(502, 'Timeout is more than 2 seconds.')

    return jsonify(results)