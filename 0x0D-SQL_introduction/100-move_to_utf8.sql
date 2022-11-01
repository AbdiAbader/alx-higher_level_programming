-- changes to utf-8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8 COLLATE utf8_unicode_ci;
ALTER TABLE first_table CHARACTER SET utf8 COLLATE utf8_unicode_ci;
ALTER TABLE first_table MODIFY name  CHARACTER SET utf8 NOT NULL COLLATE utf8_unicode_ci;