#!flask/bin/python
#from flask import Flask, jsonify, abort, request, send_from_directory, redirect, url_for
#import json
import MAX
import web_service
import wemo_env


if __name__ == '__main__':
    web_service.start()
    #wemo_env.wemo.start()
