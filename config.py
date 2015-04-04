#default config
import os
class BaseConfig(object):
	DEBUG=False
	secret_key="1234567890"
	#SQLALCHEMY_DATABASE_URI=os.environ['DATABASE_URL']

	#(LOCAL MACHINE db)'postgresql:///tweetmin'
	#for mysql :'mysql://root:eashanrocks@localhost/posts'
	#print SQLALCHEMY_DATABASE_URI
class DevelopmentConfig(BaseConfig):
	DEBUG=True