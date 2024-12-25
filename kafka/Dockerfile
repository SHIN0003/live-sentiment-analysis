FROM bitnami/kafka:3.9.0

# Use root to install packages
USER root

# Install netcat
RUN install_packages netcat || apk add --no-cache netcat-openbsd

# Revert to default user (optional)
USER 1001
