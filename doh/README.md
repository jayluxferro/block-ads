# Configure DoH

```bash
pip install doh-proxy
```

# Start DoH Proxy

```bash
doh-proxy --listen-address=127.0.0.1 --listen-port=8053 --upstream-resolver=127.0.0.1:53 --certfile=/etc/letsencrypt/live/[domain_name]/fullchain.pem --keyfile=/etc/letsencrypt/live/[domain_name]/privkey.pem
```

# Configure Nginx

```nginx
server {
    listen       443 ssl;
    http2 on;
    server_name  [domain_name];
    ssl_certificate /etc/letsencrypt/live/[domain_name]/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/[domain_name]/privkey.pem;
    ssl_session_timeout 1d;
    ssl_session_cache shared:MozSSL:10m;  # about 40000 sessions
    ssl_session_tickets off;

    # modern configuration
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers off;

    location = /dns-query  {
 proxy_pass http://127.0.0.1:8053/dns-query;
        proxy_http_version 1.1;
        proxy_set_header Host $host;

        proxy_request_buffering off;
        proxy_buffering off;
        client_max_body_size 0;
    }

    return 404;
}
```
