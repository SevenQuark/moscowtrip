

var SideBarView = Backbone.View.extend({

    events: {
        'click #clear-button': 'clearList'
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

    add_event: function(global_hot, global_name, date, fid){
        console.log(fid);


        var newVar = (global_hot + '|' + global_name + '|' + date);
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
    },

    hide_list: function(){
        this.$el.find('#empty-message').show();
        this.$el.find('#list-container').hide();
    }
});