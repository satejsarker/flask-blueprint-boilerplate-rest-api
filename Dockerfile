FROM python:3.9.13-slim
COPY dist/Flask_blueprint_boilerplate-1.0.0-py3-none-any.whl .
RUN pip3 install Flask_blueprint_boilerplate-1.0.0-py3-none-any.whl
EXPOSE 8000
#ENTRYPOINT ['simple-api']
#CMD ['--log-level','info',' --log-verbose ','waitress']
CMD simple-api --log-level info --log-verbose waitress --port 8000