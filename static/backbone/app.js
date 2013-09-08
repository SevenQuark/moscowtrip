

var SideBarView = Backbone.View.extend({

    events: {
    },

    initialize: function(){
        this.empty = true;
        this.render();
        this.count = 0;
        this.objects_list = {};
    },

    render: function(){

        var template = _.template($('#sidebar-template').html())
        this.$el.html(template({count: this.count}));
        return this;

    },

    add_event: function(global_hot, global_name, date){
        if( this.objects_list[global_name + date] < 1){
            this.objects_list[global_name + date] = 1;

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
            this.$el.find('#' + date).append(template({hot: global_hot, name: global_name, count: (global_name + date)}));
            this.$el.find('#' + this.count + ' .remove-button').on('click', $.proxy( this.remove_item, this ));
            this.count++;
        }



    },

    remove_item: function(event){
        var id = event.target.parentNode.parentNode.id;

        this.objects_list[id] = 0;
        this.$el.find('#' + id).remove();
        this.count--;

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