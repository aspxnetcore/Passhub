/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50711
 Source Host           : localhost
 Source Database       : passhub_db

 Target Server Type    : MySQL
 Target Server Version : 50711
 File Encoding         : utf-8

 Date: 05/18/2017 16:47:40 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `hub_user`
-- ----------------------------
DROP TABLE IF EXISTS `hub_user`;
CREATE TABLE `hub_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(255) DEFAULT NULL,
  `user_passwd` varchar(255) DEFAULT NULL,
  `user_mail` varchar(255) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `hub_user`
-- ----------------------------
BEGIN;
INSERT INTO `hub_user` VALUES ('1', 'admin', 'e10adc3949ba59abbe56e057f20f883e', 'lauixData@gmail.com', '2017-05-17 17:16:34');
COMMIT;

-- ----------------------------
--  Table structure for `login_log`
-- ----------------------------
DROP TABLE IF EXISTS `login_log`;
CREATE TABLE `login_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `log_title` varchar(255) DEFAULT NULL,
  `type` int(255) DEFAULT NULL COMMENT '1 成功 2失败',
  `log_desc` varchar(255) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `login_log`
-- ----------------------------
BEGIN;
INSERT INTO `login_log` VALUES ('1', '2', '登录成功', '1', '登录成功！', '2017-05-18 15:57:47');
COMMIT;

-- ----------------------------
--  Table structure for `otp_group`
-- ----------------------------
DROP TABLE IF EXISTS `otp_group`;
CREATE TABLE `otp_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_admin_id` int(11) DEFAULT NULL,
  `group_name` varchar(255) DEFAULT NULL,
  `group_desc` varchar(255) DEFAULT NULL,
  `access_id` varchar(255) DEFAULT NULL,
  `access_key` varchar(255) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `user_otp_list`
-- ----------------------------
DROP TABLE IF EXISTS `user_otp_list`;
CREATE TABLE `user_otp_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `otp_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
