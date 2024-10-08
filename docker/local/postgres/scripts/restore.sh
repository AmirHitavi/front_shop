#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

working_dir="$(dirname "${0}")"

source "${working_dir}/utils/constant.sh"
source "${working_dir}/utils/messages.sh"

if [[ -z ${1+x} ]]; then
  message_error "Backup file name is not specified yet."
  exit 1
fi

backup_filename="${BACKUP_DIR_PATH}/${1}"

if [[ ! -f ${backup_filename} ]]; then
  message_error "No backup file name with specified name was found."
  exit 1
fi

message_welcome "Restoring the ${POSTGRES_DB} database from ${backup_filename} backup."

export PGDATABASE="${POSTGRES_DB}"
export PGUSER="${POSTGRES_USER}"
export PGPASSWORD="${POSTGRES_PASSWORD}"
export PGHOST="${POSTGRES_HOST}"
export PGPORT="${POSTGRES_PORT}"

message_info "Dropping the database..."

dropdb "${PGDATABASE}"

message_info "Creating a new database..."

createdb --owner="${PGUSER}"

message_info "Applying the backups to the database..."

gunzip -c "${backup_filename}" | psql "${POSTGRES_DB}"

message_success "The '${POSTGRES_DB}' database has been restored successfully from '${backup_filename}' backup."