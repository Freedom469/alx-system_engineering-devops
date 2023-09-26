# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Define the default Nginx site configuration
file { '/etc/nginx/sites-available/default':
  ensure => 'file',
  content => "# Default Nginx site configuration\n\nserver {\n    listen 80 default_server;\n    listen [::]:80 default_server;\n\n    root /var/www/html;\n    index index.html;\n\n    server_name _;\n\n    location / {\n        return 301 http://example.com/redirect_destination;\n    }\n}\n",
  require => Package['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}

# Create an HTML file with "Hello World!" content
file { '/var/www/html/index.html':
  ensure  => 'file',
  content => '<html><body>Hello World!</body></html>',
  require => Package['nginx'],
}
