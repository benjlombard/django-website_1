

#if you have an error in ansible postregsql create db : 
#failed
fatal: [default]: FAILED! => {"failed": true, "msg": "Failed to set permissions on the temporary files Ansible needs to create when becoming an unprivileged user. For information on working around this, see https://docs.ansible.com/ansible/become.html#becoming-an-unprivileged-user"}

=> install acl : sudo apt install acl

test webhook github => execute automatically build jenkins ansible