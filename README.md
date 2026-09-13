# CloudNet-Sim
A Virtual Network & Cloud Simulator.


## Overview
Simulates cloud networking: VPCs, subnets, routing tables, firewalls, load balancers

## Features
- VPC creation
- Subnet management
- Routing simulation
- Firewall rules
- Load balancer
- Network topology visualization

## Architecture
FastAPI backend with simulation engine, React frontend for visualization

## Tech Stack
Python, FastAPI, React, Docker

## How It Works
User creates network topology via UI -> Simulation engine processes packets through rules -> Visual feedback

## Installation
docker-compose up

## Usage
Open dashboard, create VPC, add subnets, configure routes, simulate traffic

## Project Structure
- ackend/ (app/, simulation/, models/)
- rontend/ (src/)
- docker/

## Future
AWS/GCP import, traffic replay, latency simulation, Terraform export

## Screenshots
[ASCII diagram of network topology]