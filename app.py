from app import create_app

app = create_app()

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        print('Available routes:')
        for rule in app.url_map.iter_rules():
            methods = ','.join(rule.methods)
            print(f"{rule.endpoint}: {rule} [{methods}]")
    app.run(debug=True)

