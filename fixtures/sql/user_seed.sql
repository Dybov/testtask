INSERT INTO users (username, password, name, is_superuser)
VALUES
(
  'groot',
-- Already hashed password for compatibility
  'pbkdf2:sha256:260000$g17iSmQz186Tgwhi$af71779614169fe06f8d0684af166fb6d63ff7e632e3ba7d91e52ef1e896725f',
  'Groot!',
  TRUE
),
(
  'user1',
  'pbkdf2:sha256:260000$dqUbMQMkrCHWMPga$4bfd71c4933f2ee01e39355be3c2e9a6a664a6b09347510a2e8a5803ade7f431',
  'Star-Lord',
  FALSE
),
(
  'user2',
  'pbkdf2:sha256:260000$WHiF1YlSyXyh0Kge$3143b2e4bc04370c551d74d9032e101cc535f69f5602a35e985ef2daa715f96d',
  'Gamora',
  FALSE
),
(
  'user3',
  'pbkdf2:sha256:260000$rcVdwRjq8X0OdkMx$80b9abf231f55f25f2c5509563aa25b8cb91d8789f55aef6b3387edcafab3b11',
  'Rocket Racoon',
  FALSE
);
