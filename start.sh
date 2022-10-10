if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/ritheshrkrm/EvaFileFilterBot.git /EvaMariaBot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /EvaMariaBot
fi
cd /EvaMaria
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py