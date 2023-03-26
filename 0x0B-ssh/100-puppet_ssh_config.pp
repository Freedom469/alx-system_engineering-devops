#PUPPET Script to creat ssh config file

file {'/etc/ssh/ssh_config':

    ensure  => 'file',
    content => "
                IdentityFile ~/.ssh/school
                PasswordAuthentication no

                ",

    }
