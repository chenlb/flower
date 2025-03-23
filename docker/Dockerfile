FROM langfarm/python:3.12.9

ARG FLOWER_HOME=/home/admin/flower

RUN mkdir -p ${FLOWER_HOME}

WORKDIR ${FLOWER_HOME}

COPY . ./

# build
ARG PYTHON_HOME=/home/admin/.local
RUN uv venv ${PYTHON_HOME} --seed
RUN uv pip install --directory ${PYTHON_HOME} --no-cache-dir -r ${FLOWER_HOME}/requirements/default.txt
RUN uv pip install --directory ${PYTHON_HOME} --no-cache-dir setuptools
RUN ${PYTHON_HOME}/bin/python setup.py build
RUN ${PYTHON_HOME}/bin/python setup.py install

# rm build dist
RUN rm -rf ./build ./dist ./flower.egg-info

# Install the run required packages
RUN uv pip install --directory ${PYTHON_HOME} --no-cache-dir redis

# PYTHONUNBUFFERED: Force stdin, stdout and stderr to be totally unbuffered. (equivalent to `python -u`)
# PYTHONHASHSEED: Enable hash randomization (equivalent to `python -R`)
# PYTHONDONTWRITEBYTECODE: Do not write byte files to disk, since we maintain it as readonly. (equivalent to `python -B`)
ENV PYTHONUNBUFFERED=1 PYTHONHASHSEED=random PYTHONDONTWRITEBYTECODE=1

RUN chown -R admin:admin /home/admin

RUN chmod +x ./entrypoint.sh

USER admin

# Default port
EXPOSE 5555

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["./entrypoint.sh"]
