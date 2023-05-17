-- creates the  user user_zapel_1 and grant all priviledges
CREATE USER IF NOT EXISTS user_zapel_1@localhost IDENTIFIED BY 'user_zapel_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO user_zapel_1@localhost;
