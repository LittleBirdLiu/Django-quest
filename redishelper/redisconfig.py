#coding=utf-8
import redis
from django.conf import settings

#redis库
QUESTION_DB_NUM=3
TIME_LINE_DB_NUM=2
USER_INFO_DB_NUM=1

EMAIL_LIST_PREFIX="email:"

QUESTION_FOLLOWER_PREFIX="question_follower:"#问题的关注者set
QUESTION_PRFIX="followquestion:"#问题关注hash
QUESTION_PRFIX="question:"#问题信息 hash
ANSWER_PRFIX="answer:"#答案 hash
COMMENT_PRFIX="comment:"#评论hash

ANSWEREVALUATION_PRFIX="answerevaluation:"#评价 hash
OPPOSE_ANSWEREVALUATION_PRFIX="fanswerevaluation:"#赞成问题的用户id set
FAVOUR_ANSWEREVALUATION_PRFIX="panswerevaluation:"
QUESTION_ANSWER_PREFIX="question_answer:"#问题的回答id列表
ANSWER_COMMENT_PREFIX="answer_comment:"#回答的评论id列表
ANSWER_EVALUATION_PREFIX="answer_evaluation:"


CURRENT_ACTIVITY_ID_PREFIX="current_activity_id"
CURRENT_EVENT_ID_PREFIX="current_event_id"
CURRENT_MESSAGE_ID_PREFIX="current_message_id"
CURRENT_ACTIVITY_ID_PREFIX="current_activity_id"
CURRENT_EVENT_ID_PREFIX="current_event_id"
CURRENT_MESSAGE_ID_PREFIX="current_message_id"
CURRENT_QUESTION_ID_PREDIX="current_question_id"
CURRENT_ANSWER_ID_PREDIX="current_answer_id"
CURRENT_COMMENT_ID_PREDIX="current_comment_id"
CURRENT_QUESTION_FOLLOW_ID_PREDIX="current_question_follow_id"
CURRENT_ANSWER_EVALUATION_ID_PREDIX="current_answer_evaluation_id"
CURRENT_COMMENT_EVALUATION_ID_PREDIX="current_comment_evaluation_id"

USER_UNREAD_MESSAGE_TIME_LINE_PREFIX="message_unread_time_line:"
USER_UNREAD_MESSAGE_PREFIX="unread_message:"
USER_UNREAD_MESSAGE_COUNT_PREFIX="unread_message_count:"


USER_HASH_PREFIX="user:"
USER_FOLLOW_PREFIX="follow:"
USER_FOLLOWER_PREFIX="follower:"
USER_FAVOR_ANSWER_PREFIX="answer_favor:" #用户赞过的问题set
USER_OPPOSE_ANSWER_PREFIX="answer_oppose:"#用户反对过得问题set
USER_FOLLOW_QUESTION_PREFIX="qfollow:"
USER_EVENT_TIME_LINE_PREFIX="event_time_line:"
USER_ACTIVITY_TIME_LINE_PREFIX="activity_time_line:"
USER_MESSAGE_TIME_LINE_PREFIX="message_time_line:"
USER_UNREAD_MESSAGE_TIME_LINE_PREFIX="message_unread_time_line:"
USER_UNREAD_MESSAGE_PREFIX="unread_message:"
USER_UNREAD_MESSAGE_COUNT_PREFIX="unread_message_count:"
USER_EVENT_TIME_LINE_PREFIX="event_time_line:"
USER_ACTIVITY_PREFIX="activity:"
USER_MESSAGE_PREFIX="message:"
USER_EVENT_PREFIX="event:"

TEMP_PREFIX="temp:"
TIME_STRF="%Y/%m/%d %H:%M:%S"
FAVOR_ANSWER=1
OPPOSE_ANSWER=2
SPLIT_STR="t:"
ACTIVITY_TYPE={"submit_question":0,"add_answer":1,"follow_question":2,"evaluate_answer":3,"reply_answer":4,"reply_comment":5,"follow_user":6}


timeline_client=redis.StrictRedis(host=settings.REDIS_IP,port=settings.REDIS_PORT,db=TIME_LINE_DB_NUM)
question_client=redis.StrictRedis(host=settings.REDIS_IP,port=settings.REDIS_PORT,db=QUESTION_DB_NUM)
user_client=redis.StrictRedis(host=settings.REDIS_IP,port=settings.REDIS_PORT,db=USER_INFO_DB_NUM)
