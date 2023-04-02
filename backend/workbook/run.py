from workbook.app import app
from workbook.route import init_routes
# add controllers here

# setting up routes
init_routes()


if __name__ == '__main__':
    app.run(debug=True)
