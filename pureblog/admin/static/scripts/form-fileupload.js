var FormFileUpload = function () {
    return {
        init: function () {
            String.prototype.endWith=function(str){
              var reg=new RegExp(str+"$");
              return reg.test(this);
            };

            function checkSize(value){
                // 文件大小限制为10M
                return value<10*1024;
            }
            $("#posts-file").change(function(){
                var files = $(this).context.files;
                if (files.length > 0){
                    var file = files[0];
                    var name = file.name;
                    var size = file.size;
                    if (!name.endWith('.md')){
                        Common.notify('error', '上传文件格式错误，只能上传markdown文件', '');
                    }else if (!checkSize(size)){
                        Common.notify('error', '上传文件格大小超过限制，单个文件小于10M', '');
                    } else {
                        var html = '<span style="margin-left: 2em;"><span>'+name+'</span> ' +
                            '<button class="btn blue start" style="margin-left: 1em;"> ' +
                            '<i class="fa fa-upload"></i> ' +
                            '<span class="btn-upload">上传</span> </button></span>';
                        $('.fileinput-button').after(html);
                        var $title = $("input[name='title']");
                        if ($title.val() === '') {
                            $title.val(name.substring(0, name.length-3));
                        }
                    }
                }
            });

            $(".btn-upload").click(function(){
                $.ajaxFileUpload({
                    url : Website.upload_file,
                    secureuri : false,
                    fileElementId : 'posts-file',
                    dataType : 'text',
                    success : function(data, status) {
                        console.log(data);
                    },
                    error : function(data, status, e) {
                        console.log(data);
                    }
                });
            });
        }
    };
}();