var postsWrite = function(){
    return {
        init: function(){
            function validate(){
                var title = $("input[name='title']").val();
                var summary = $("textarea[name='summary']").val();
                //var posts_category = $("select[name='posts_category']").val();
                var posts_name = $("input[name='posts_name']").val();
                //var is_public = $("input[name='is_public']:checked").val();
                console.log(title, summary, posts_name);
                var flag = true;
                if (title === ''){
                    $(".txt-error").text("文章标题不可为空");
                }else if(summary === ""){
                    $(".txt-error").text("摘要不可为空");
                }else if(posts_name === ""){
                    $(".txt-error").text("文章不可为空");
                }else{
                    $('.alert-danger').addClass('display-none');
                    flag = false;
                }

                if(flag){
                    $('.alert-danger').removeClass('display-none');
                }
                return flag;
            }

            $(".btn-save").click(function(){
                if(!validate()){
                    var title = $("input[name='title']").val();
                    var summary = $("textarea[name='summary']").val();
                    var posts_category = $("select[name='posts_category']").val();
                    var posts_name = $("input[name='posts_name']").val();
                    var is_public = $("input[name='is_public']:checked").val();
                    var csrf_token = $("#csrf_token").val();
                    var args = {
                        title: title,
                        summary: summary,
                        posts_category: posts_category,
                        posts_name: posts_name,
                        is_public: is_public,
                        csrf_token: csrf_token
                    };
                    Common.ajaxPost(Website.posts_write, args, function(result){
                        if(result.code === 0){
                            Common.notify('success', '文章保存成功！', '');
                            window.location.href = Website.posts_list;
                        }else{
                            Common.notify('error', result.error, '');
                        }
                    });
                }
            });
        }
    }
}();