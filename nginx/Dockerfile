FROM nginx

#RUN rm /etc/nginx/nginx.conf
#COPY nginx.conf /etc/nginx/
RUN rm /etc/nginx/conf.d/default.conf
COPY sites-enabled/www.lvh.me /etc/nginx/conf.d/


#FROM tutum/nginx
#RUN rm /etc/nginx/sites-enabled/default
#ADD sites-enabled/ /etc/nginx/sites-enabled
