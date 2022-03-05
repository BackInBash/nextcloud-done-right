docker run \
-e SMASHBOX_URL=127.0.0.1 \
-e SMASHBOX_USERNAME=admin \
-e SMASHBOX_PASSWORD=admin \
-e SMASHBOX_ACCOUNT_PASSWORD=admin \
-e SMASHBOX_TEST_NAME=nplusone \
-v ~/smashdir:/smashdir \
-v /tmp:/tmp \
owncloud/smashbox:build