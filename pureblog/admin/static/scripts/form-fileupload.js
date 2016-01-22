var FormFileUpload = function () {
    return {
        init: function () {
            String.prototype.endWith=function(str){
              var reg=new RegExp(str+"$");
              return reg.test(this);
            };

            function checkSize(value){
                // 文件大小限制为10M
                return value<10*1024*1024;
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
                        var html = '<span class="upload-file-area" style="margin-left: 2em;"><span>'+name+'</span> ' +
                            '<button class="btn blue start" style="margin-left: 1em;"> ' +
                            '<i class="fa fa-upload"></i> ' +
                            '<span class="btn-upload">上传</span> </button></span>';
                        $(".upload-file-area").remove();
                        $('.fileinput-button').after(html);
                        var $title = $("input[name='title']");
                        if ($title.val() === '') {
                            $title.val(name.substring(0, name.length-3));
                        }
                    }
                }
            });
            $('.form-group').delegate('.btn-upload', 'click', function(e){
                e.stopPropagation();
                var files = document.getElementById('posts-file').files;
                if (files.length > 0){
                    var file = files[0];
                    console.log(file);

                    // FormData 对象
                    var form = new FormData();
                    form.append("posts_file", file);

                    // XMLHttpRequest 对象
                    var xhr = new XMLHttpRequest();
                    xhr.open("post", Website.upload_file, true);
                    xhr.onload = function () {
                        alert("上传完成!");
                    };

                    xhr.upload.addEventListener("progress", progressFunction, false);
                    xhr.send(form);
                    return false;
                }
                return false;
            });
            function progressFunction(e) {
                console.log(e);
                //var progressBar = document.getElementByIdx_x_x("progressBar");
                //var percentageDiv = document.getElementByIdx_x_x("percentage");
                //if (evt.lengthComputable) {
                //    progressBar.max = evt.total;
                //    progressBar.value = evt.loaded;
                //    percentageDiv.innerHTML = Math.round(evt.loaded / evt.total * 100) + "%";
                //}
            }
        }
    };
}();