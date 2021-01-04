#基于的基础镜像
FROM python:3

#定义时区参数
ENV TZ=Asia/Shanghai

#设置时区
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ADD ./sources.list /etc/apt/sources.list

RUN apt-get update

RUN apt-get install -y vim

#代码添加到code文件夹
ADD ./ /usr/src/app
#添加pip国内镜像
ADD ./pip.conf /root/.pip/pip.conf

# 设置app文件夹是工作目录
WORKDIR /usr/src/app

# 安装支持
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "/usr/src/app/main.py" ]