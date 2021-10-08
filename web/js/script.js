$("#search_btn").on("click", function(){
    const search_keyword = search_word.value
    if (search_keyword) {
      async function run() {
        const news_list = await eel.get_item_list(search_keyword)();
        if(news_list) {
          create_table(news_list)
        } else {
          alert("エラー")
        }
      }
      run();
    } else {
      alert("キーワードを入力してください。")
    }
  })
  
  $("#output").on("click", function() {
    let items = []
    $('.form-check-input').each((i,e)=>{
      if($(e).is(':checked')) {
        items.push(e.value)
      }
    });

    if(items) {
      async function run() {
        await eel.check_and_tweet(items)();
      }
      run();
    } else {
      alert("商品が未選択です。")
    }
  })
  
  function create_table(items) {
    $("#item_list").remove()
    let html = "<tbody id='item_list'>"
    for (i in items[0]) {
      html += "<tr>"
        html += "<td><input type='checkbox' class='form-check-input' value='" + items[0][i] + "'/></td>"
        html += "<td>"
          html += "<img class='pict' src='" + items[1][i] + "' alt=''>"
        html += "</td>"
        html += "<td>"
          html += "<a href='" + items[3][i] +"' target='_blank'>"
            html += items[2][i]
          html += "</a>"
        html += "</td>"
        html += "<td>" + items[0][i] + "</td>"
      html += "</tr>"
    }
    html += "</tbody>"
    $(".table").append(html)
  }