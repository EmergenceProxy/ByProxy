#!/bin/bash

# --- Configuration ---
# Your desired tag key prefix (e.g., "web-server-")
TAG_KEY_PREFIX="ytcdl-web-server-"

# The ID of the EC2 instance to tag
INSTANCE_ID="i-0abcdef1234567890"

# The AWS region where your instances are located
AWS_REGION="us-east-2"
# ---------------------

echo "Finding the highest incremented number for tag key: $TAG_KEY_PREFIX"

# Get all 'Name' tags that match the prefix.
# The query extracts the numeric part of the tag value, if present.
HIGHEST_NUMBER=$(aws ec2 describe-tags \
  --filters "Name=key,Values=Name" "Name=value,Values=$TAG_KEY_PREFIX*" \
  --query "Tags[].Value" \
  --output text \
  --region "$AWS_REGION" | \
  grep -oP '\d+$' | \
  sort -n | \
  tail -1)

# Set the counter based on the highest number found.
if [[ -z "$HIGHEST_NUMBER" ]]; then
    NEW_COUNTER=1
else
    NEW_COUNTER=$((HIGHEST_NUMBER + 1))
fi

echo "Next available number is: $NEW_COUNTER"

# Define the new tag value
NEW_TAG_VALUE="$TAG_KEY_PREFIX$NEW_COUNTER"

echo "Applying tag 'Name=$NEW_TAG_VALUE' to instance $INSTANCE_ID"

# Apply the new tag to the instance
aws ec2 create-tags \
  --resources "$INSTANCE_ID" \
  --tags "Key=Name,Value=$NEW_TAG_VALUE" \
  --region "$AWS_REGION"

if [ $? -eq 0 ]; then
    echo "Tag successfully applied."
else
    echo "Failed to apply tag." >&2
    exit 1
fi
