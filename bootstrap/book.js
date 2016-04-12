var main = function () {
	$('.btn-updateBook').click(function(event) {
	$('.sql').toggle()
	$.getJSON('book.json',function(jd) {
	$('.buyBook').text(jd.Buy);
	$('.sellBook').text(jd.Sell);
});
});
};
var err = function () {
    $.getJSON("book.json", function(d) {
        alert("success");
    }).fail( function(d, textStatus, error) {
        console.error("getJSON failed, status: " + textStatus + ", error: "+error)
    });
}
$(document).ready(main);
