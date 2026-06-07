# Automated Outreach Pipeline

## Overview

This project automates the B2B outreach workflow using multiple APIs.

Pipeline Flow:

1. Input a company domain
2. Find similar companies using Ocean.io
3. Discover contacts using Prospeo
4. Process outreach through Brevo

## Technologies Used

* Python
* Ocean.io API
* Prospeo API
* Brevo API

## Project Structure

* main.py
* ocean.py
* prospeo.py
* brevo.py
* config.py

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Example Input

```text
zoho.com
```

## Features

* Similar company discovery
* Contact enrichment
* Outreach automation pipeline
* CLI based workflow
