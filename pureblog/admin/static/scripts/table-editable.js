var TableEditable = function () {

    var handleTable = function () {

        function restoreRow(oTable, nRow) {
            var aData = oTable.fnGetData(nRow);
            var jqTds = $('>td', nRow);
            for (var i = 0, iLen = jqTds.length; i < iLen; i++) {
                oTable.fnUpdate(aData[i], nRow, i, false);
            }
            oTable.fnDraw();
        }

        function editRow(oTable, nRow) {
            var aData = oTable.fnGetData(nRow);
            var jqTds = $('>td', nRow);
            jqTds[0].innerHTML = '<input type="text" class="form-control input-small" value="' + aData[0] + '">';
            jqTds[1].innerHTML = '<a class="edit" href="">保存</a>';
            jqTds[2].innerHTML = '<a class="cancel" href="">取消</a>';
        }

        function saveRow(oTable, nRow) {
            var jqInputs = $('input', nRow);
            var category_name = jqInputs[0].value;
            var category_id = $(nRow).attr('data-id');
            console.log(category_id, category_name);
            Common.ajaxPost(Website.category_update,
                    {category_id: category_id, category_name: category_name},
                    function(data){
                        if(data.code === 0){
                            Common.notify('success', data.data, '');
                            oTable.fnUpdate(jqInputs[0].value, nRow, 0, false);
                            oTable.fnUpdate('<a class="edit" href="">编辑</a>', nRow, 1, false);
                            oTable.fnUpdate('<a class="delete" href="">删除</a>', nRow, 2, false);
                            oTable.fnDraw();
                        }else{
                            Common.notify('error', data.error, '');
                        }
                    });

        }

        function cancelEditRow(oTable, nRow) {
            var jqInputs = $('input', nRow);
            oTable.fnUpdate(jqInputs[0].value, nRow, 0, false);
            oTable.fnUpdate('<a class="edit" href="">编辑</a>', nRow, 1, false);
            oTable.fnDraw();
        }

        var table = $('#category_list');

        var oTable = table.dataTable({
            "lengthMenu": [
                [5, 15, 20, -1],
                [5, 15, 20, "全部"] // change per page values here
            ],

            // Or you can use remote translation file
            //"language": {
            //   url: '//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/English.json'
            //},

            // set the initial value
            "pageLength": 15,

            "language": {
                "sEmptyTable": "没有可用的数据",
                "sInfo": "当前 _START_ ~ _END_ ，共 _TOTAL_ 条记录",
                "sInfoEmpty": "有0条记录",
                "sInfoFiltered": "(从 _MAX_ 条记录中筛选)",
                "sInfoPostFix": "",
                "sInfoThousands": ",",
                "sLengthMenu": "每页 _MENU_ 条记录",
                "sLoadingRecords": "加载中...",
                "sProcessing": "处理中...",
                "sSearch": "查找:",
                "sZeroRecords": "没有查找到符合要求的记录",
                "oPaginate": {
                    "sFirst": "首页",
                    "sLast": "末页",
                    "sNext": "下一页",
                    "sPrevious": "上一页"
                },
                "oAria": {
                    "sSortAscending": ": activate to sort column ascending",
                    "sSortDescending": ": activate to sort column descending"
                }
            },

            "columnDefs": [{
                'orderable': true,
                'targets': [0]
            }, {'orderable': false, 'targets': [1, 2]},
                {
                    "searchable": true,
                    "targets": [0]
                }],
            "order": [
                [0, "asc"]
            ] // set first column as a default sort by asc
        });

        var nEditing = null;
        var nNew = false;

        table.on('click', '.delete', function (e) {
            e.preventDefault();
            if (confirm("确定删除这一行记录 ?")) {
                var nRow = $(this).parents('tr')[0];
                var category_id = $(nRow).attr('data-id');
                Common.ajaxPost(Website.category_delete, {category_id: category_id}, function(data){
                    if(data.code === 0){
                        Common.notify('success', data.data, '');
                        oTable.fnDeleteRow(nRow);
                    } else{
                        Common.notify('error', data.error, '');
                    }
                });
            }
        });

        table.on('click', '.cancel', function (e) {
            e.preventDefault();
            if (nNew) {
                oTable.fnDeleteRow(nEditing);
                nEditing = null;
                nNew = false;
            } else {
                restoreRow(oTable, nEditing);
                nEditing = null;
            }
        });

        table.on('click', '.edit', function (e) {
            e.preventDefault();
            /* Get the row as a parent of the link that was clicked on */
            var nRow = $(this).parents('tr')[0];
            if (nEditing !== null && nEditing != nRow) {
                /* Currently editing - but not this row - restore the old before continuing to edit mode */
                restoreRow(oTable, nEditing);
                editRow(oTable, nRow);
                nEditing = nRow;
            } else if (nEditing == nRow && this.innerHTML === "保存") {
                /* Editing this row and want to save it */
                saveRow(oTable, nEditing);
                nEditing = null;
            } else {
                /* No edit in progress - let's start one */
                editRow(oTable, nRow);
                nEditing = nRow;
            }
        });
    };

    return {
        init: function () {
            handleTable();
        }

    };

}();