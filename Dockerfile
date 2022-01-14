FROM public.ecr.aws/lambda/python:3.9

RUN pip3 install poetry

COPY app ${LAMBDA_TASK_ROOT}/app
# COPY output ${LAMBDA_TASK_ROOT}/output

WORKDIR ${LAMBDA_TASK_ROOT}/app
RUN poetry export -f requirements.txt --output requirements.txt && \
    pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

CMD [ "app.app.main.handler" ]