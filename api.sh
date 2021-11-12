#!/usr/bin/env bash

function get_repos() {
  repos=`curl -s -H $token "https://api.github.com/users/$user_git/repos" | jq -j '.[] | "\n", "- ", .name'`
  echo -e "Repositorios de $user_git: $repos"
}

function get_contributors(){
  r_contributors=`curl -s -H $token "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" "https://api.github.com/repos/$user_git/$repositorio/contributors" | jq -j '.[] | .login, ", "'`
  echo -e "Contribuyentes: $r_contributors"
}

function get_info() {
  curl -s -H $token "https://api.github.com/repos/$user_git/$repositorio" | jq -j '"url_repo: ", .html_url, "\n"'
  curl -s -H $token "https://api.github.com/repos/$user_git/$repositorio" | jq -j '"ssh_url: ", .ssh_url, "\n"'
  curl -s -H $token "https://api.github.com/repos/$user_git/$repositorio" | jq -j '"created_at: ", .created_at, "\n"'
}

user_git=$1
repositorio=$2
token=$3

get_repos
get_contributors
echo -e "Información del repositorio:"
get_info
