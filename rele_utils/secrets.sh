sudo mkdir -p /etc/releai/keys
echo "$DEV_SECRETS" | base64 --decode > $GITHUB_WORKSPACE/ops/keys/releai-bot-dev.json
echo "$PROD_SECRETS" | base64 --decode > $GITHUB_WORKSPACE/ops/keys/releai-bot-prod.json
sudo cp -r $GITHUB_WORKSPACE/ops/keys/releai-bot-dev.json /etc/releai/keys/releai-bot-dev.json
sudo cp -r $GITHUB_WORKSPACE/ops/keys/releai-bot-prod.json /etc/releai/keys/releai-bot-prod.json
