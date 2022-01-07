$(function() {
    $('.delete-button').click(function(event){
      event.preventDefault();
      // Use the same link. Back-end will figure out if it is AJAX
      var link = this.href;
      $.getJSON(
        link,
        function(data){
          $('#row-' + data.deleted).remove();
          // Reload page if deleted user is current user
          if (data.deleted == $CURRENT_USER_ID) {
            location.reload();
          }
        }
      ).fail(function(XHR) {
        if (XHR.status == 403){
          alert("403 AJAX request is forbidden.")
        } else {
          alert("Uncatched error at AJAX request.")
        }
      });
    });
  });