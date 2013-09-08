

var SideBarView = Backbone.View.extend({

    events: {
    },

    initialize: function(){
        this.empty = true;
        this.render();
        this.count = 0;
        this.objects_list = {};
        this.count_list = {};
    },

    render: function(){

        var template = _.template($('#sidebar-template').html())
        this.$el.html(template({count: this.count}));
        return this;

    },

    add_event: function(global_hot, global_name, date){


        var newVar = (global_hot + global_name + date);
        if( this.objects_list[  newVar ] == 0 || this.objects_list[newVar] == undefined){
            this.objects_list[newVar] = 1;
            this.count_list[this.count] = newVar;

            var bar = $('#fluidSidebar');
            if(bar.is(':hidden')){
                bar.show();
                bar.animate({
                    right:0
                });
            }

            if( !this.count){
                this.empty = false;
                this.show_list();
            }

            var template = _.template($('#list-item').html());

            this.$el.find('#' + date).append(template({hot: global_hot, name: global_name, count: this.count}));
            this.$el.find('#' + this.count+ ' .remove-button').on('click', $.proxy( this.remove_item, this ));
            this.count++;
        }



    },

    remove_item: function(event){
        var id = event.target.parentNode.parentNode.id;

        this.$el.find('#' + id).remove();
        this.count--;

        var key = this.count_list[id];
        this.objects_list[key] = 0;

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