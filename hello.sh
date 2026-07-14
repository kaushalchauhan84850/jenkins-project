echo "Welcome to the Jenkins Hell📁"
echo "user : $(hostname)"
echo "Hostname : $(hostname)"
echo "Currnet Dir : $(pwd)"
echo "Date : $(date)"
echo "Installing Updates"
sudo apt update
sudo apt install -y nginx
nginx -version
