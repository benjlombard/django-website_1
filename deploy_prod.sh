#!/bin/bash
#ansible-playbook ./deploy.yml --private-key=~/.ssh/id_rsa_rhs  -K -e ansible_ssh_port=4575 -u mlsuyt2718 -i ./hosts
#ansible-playbook ./prod/deploy.yml --private-key=~/.ssh/id_rsa_rhs -K -u mlsuyt2718 -i ./prod/hosts

#variable d'environnement contenant un password pour que l'automatisation de l'installationd de jenkins fonctionne, donc plus besoin du -K
ansible-playbook ./prod/deploy.yml --private-key=~/.ssh/id_rsa_rhs -u mlsuyt2718 -i ./prod/hosts