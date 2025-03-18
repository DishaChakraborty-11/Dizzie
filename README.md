      # python code to generate fun facts


     from pywebio.output import put_html, put_buttons, clear, style
      import json
      import requests

    def get_fun_fact(_):
       clear()
    
    # Add custom CSS styling
    put_html("""
    <style>
        body {
            background-color: #f4f4f4;
            font-family: Arial, sans-serif;
        }
        .fact-container {
            text-align: center;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            margin: auto;
            width: 50%;
        }
        .fun-fact {
            font-size: 24px;
            color: #3498db;
            font-weight: bold;
        }
        .btn {
            background-color: #28a745;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 5px;
            border: none;
            cursor: pointer;
        }
        .btn:hover {
            background-color: #218838;
        }
    </style>
    """)

    put_html('<div class="fact-container">')
    
    # API request
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response = requests.get(url)
    data = json.loads(response.text)
    
    useless_fact = data['text']
    
    put_html(f'<p class="fun-fact">{useless_fact}</p>')
    
    put_buttons(
        [dict(label='Click me', value='outline-success', color='outline-success')],
        onclick=get_fun_fact
    )
    
    put_html('</div>')

     if __name__ == '__main__':
          put_html('<h2 style="text-align:center;">Fun Fact Generator</h2>')
    
    put_buttons(
        [dict(label='Click me', value='outline-success', color='outline-success')],
        onclick=get_fun_fact
    )

