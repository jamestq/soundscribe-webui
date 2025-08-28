#!/bin/bash
$(docker compose -f local.yml ps -q postgres)
docker cp backups/initial.sql.gz $(docker compose -f local.yml ps -q postgres):/backups 
docker stop $(docker compose -f local.yml ps -q webui)
docker compose -f local.yml exec postgres restore initial.sql.gz
docker compose -f local.yml up -d --no-deps