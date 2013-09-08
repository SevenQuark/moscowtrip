

var SideBarView = Backbone.View.extend({

    events: {
    },

    initialize: function(){
        this.render();
        this.count = 0;
        this.objects_list = {};
        this.count_list = {};
        this.date_count = {};
    },

    render: function(){

        var template = _.template($('#sidebar-template').html())
        this.$el.html(template({count: this.count}));

        this.$el.find('#clear-button').on('click', $.proxy( this.clearList, this ));
        $('#send-plan').on('click', $.proxy( this.send_mail, this ));
        return this;

    },

    clearList: function(event){
        for( var i=0; i<this.count; i++){
            this.$el.find('#' + i).remove();

        }
        this.count = 0;
        this.objects_list = {};
        this.count_list = {};
        this.date_count = {};

        this.hide_list();

    },

    send_mail: function(){
        var fid_list = [];

        var count = 0;
        for(var id in this.objects_list){
            var fid = id.split('|')[3]
            var date = id.split('|')[2]
            fid_list.push([fid, date]);
            count++;

        }

        current_url = document.URL

        var email = $('#email').val()
        var data = {};
        data['email'] = email
        data['fidsday'] = fid_list;

        var send = {data: JSON.stringify(data)};

        $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie !== '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        if (cookie.substring(0, name.length + 1) === (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
            }
        }
        });

        $.post('/get_plan/', send, function(data, textStatus) {
          //data contains the JSON object
          //textStatus contains the status: success, error, etc
        });



    },

    add_event: function(global_hot, global_name, date, fid){
        var newVar = (global_hot + '|' + global_name + '|' + date + '|' + fid);
        if( this.objects_list[newVar] == undefined){

            this.count_list[this.count] = newVar;
            if(this.date_count[date]){
                this.date_count[date] += 1;

            }else{
                this.date_count[date] = 1;

            }

            var bar = $('#fluidSidebar');
            if(bar.is(':hidden')){
                bar.show();
                bar.animate({
                    right:0
                });
            }

            if( !this.count){
                this.show_list();
            }

            var template = _.template($('#list-item').html());

            var element = this.$el.find('#' + date).append(template({hot: global_hot, name: global_name, count: this.count}));
            this.objects_list[newVar] = element;

            this.$el.find('#' + date + '-').html(this.date_count[date]);
            this.$el.find('#' + this.count + ' .remove-button').on('click', $.proxy( this.remove_item, this ));
            this.count++;
        }



    },

    remove_item: function(event){
        var id = event.target.parentNode.parentNode.id;

        this.$el.find('#' + id).remove();
        this.count--;



        var key = this.count_list[id];
        this.objects_list[key] = undefined;
        var params = key.split('|');
        var date = params[2];
        this.date_count[date]--;
        this.$el.find('#' + date + '-').html(this.date_count[date]);

        if( !this.count ){
            this.hide_list();
        }
    },

    show_list: function(){
        this.$el.find('#empty-message').hide();
        this.$el.find('#list-container').show();
        $('#planBar').show();
    },

    hide_list: function(){
        this.$el.find('#empty-message').show();
        this.$el.find('#list-container').hide();
        $('#planBar').hide();
    }
});