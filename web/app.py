from flask import Flask, request, render_template, Response
import subprocess
import time
from utils import Utils

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/groupon")
def get_groupon():
    # Get parameters
    location_id = request.args.get('location')
    query = request.args.get('query')

    # Remove file if it already exists
    Utils.remove_file('../crawler/results/groupon.json')

    # Process crawl groupon
    scrapy_url = 'scrapy crawl groupon -a location=%s -a query="%s" -o results/groupon.json' \
                 % (Utils.get_location(location_id).get_groupon_name(), query)
    subprocess.call('cd ../crawler && ' + scrapy_url, shell=True)

    # Wait 4 seconds
    time.sleep(4)

    # Get file content for groupon
    text = Utils.get_file_content('../crawler/results/groupon.json')

    # Generate Response
    return Response(response=text, mimetype='application/json', status=200)


@app.route("/groupalia")
def get_groupalia():
    # Get parameters
    location_id = request.args.get('location')
    query = request.args.get('query')

    # Remove file if it already exists
    Utils.remove_file('../crawler/results/groupalia.json')

    # Process crawl groupalia
    scrapy_url = 'scrapy crawl groupalia -a location=%s -a query="%s" -o results/groupalia.json' \
                 % (Utils.get_location(location_id).get_groupalia_name(), query)
    subprocess.call('cd ../crawler && ' + scrapy_url, shell=True)

    # Wait 4 seconds
    time.sleep(4)

    # Get file content for groupalia
    text = Utils.get_file_content('../crawler/results/groupalia.json')

    # Generate Response
    return Response(response=text, mimetype='application/json', status=200)


@app.route("/lets_bonus")
def get_lets_bonus():
    # Get parameters
    location_id = request.args.get('location')
    query = request.args.get('query')

    # Remove file if it already exists
    Utils.remove_file('../crawler/results/lets_bonus.json')

    # Process crawl lets bonus
    scrapy_url = 'scrapy crawl lets_bonus -a location=%s -a query="%s" -o results/lets_bonus.json' \
                 % (Utils.get_location(location_id).get_lets_bonus_name(), query)
    subprocess.call('cd ../crawler && ' + scrapy_url, shell=True)

    # Wait 4 seconds
    time.sleep(4)

    # Get file content for lets bonus
    text = Utils.get_file_content('../crawler/results/lets_bonus.json')

    # Generate Response
    return Response(response=text, mimetype='application/json', status=200)


if __name__ == "__main__":
    app.run()
