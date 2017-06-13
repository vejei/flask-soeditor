function SOEditor(textareaId) {
	var style = css($(textareaId))
	$(textareaId).replaceWith('<div class="wmd-panel">' + 
    	'<div id="wmd-button-bar" class="wmd-button-bar">' + 
    	'</div><textarea class="wmd-input" id="wmd-input">' + 
    	'</textarea></div><div id="wmd-preview" ' + 
    	'class="wmd-panel wmd-preview markdown-body"></div>');
	$(".wmd-panel").css(style)

	var converter = Markdown.getSanitizingConverter();
    var helpUrl = 'https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet'
    var help = function() {
    	window.open(helpUrl, '_blank');
    }
    var options = {
        helpButton: {handler: help},
        strings: {quoteexample: "Blockquote"}
    };
    
    var editor = new Markdown.Editor(converter, "", options);
    editor.run();
}