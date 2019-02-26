##### 1. 添加nginx到yum源

> `sudo rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm`

##### 2. 安装nginx

> `sudo yum install -y nginx`

##### 3. 启动nginx

> `sudo systemctl start nginx.service`

##### 4. 开机启动nginx

> `sudo systemctl enable nginx.service`

##### 5. nginx配置信息

> ```
> 静态文件存放目录
> /usr/share/nginx/html
> 
> nginx全局配置
> /etc/nginx/nginx.conf
> 
> 自定义nginx配置文件
> /etc/nginx/conf.d/
> ```

##### 6. 启动nginx

> `nginx -c nginx.conf`

