var editor = new MediumEditor('.editable', 
            {
                toolbar: {
                /* These are the default options for the toolbar,
                if nothing is passed this is what is used */
                allowMultiParagraphSelection: true,
                buttons: ['bold', 'italic', 'underline', 'anchor', 'h1', 'h2','p', 'h3' , 'quote'],
                diffLeft: 0,
                diffTop: -10,
                firstButtonClass: 'medium-editor-button-first',
                lastButtonClass: 'medium-editor-button-last',
                relativeContainer: null,
                standardizeSelectionStart: false,
                static: false,
                /* options which only apply when static is true */
                align: 'center',
                sticky: false,
                updateOnEmptySelection: false
                }
            });
        
            editor.subscribe('editableInput', function (event, editable) {
            var x = editable.innerHTML; // editable is the editor <div> element that was changed
            var y = editor.getContent(); // getContent() returns the content of the editor as well
            console.log(x)
            console.log(y)
            });

 