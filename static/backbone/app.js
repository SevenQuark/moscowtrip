

var SideBarView = Backbone.View.extend({

    events: {
    },

    initialize: function(){
        this.empty = true;
        this.render();
        this.count = 0;
    },

    render: function(){

        var template = _.template($('#sidebar-template').html())
        this.$el.html(template({count: this.count}));
        return this;

    },

    add_event: function(global_hot, global_name, date){

        if( !this.count){
            this.empty = false;
            this.show_list();
        }

        var template = _.template($('#list-item').html());
        this.$el.find('#' + date).append(template({hot: global_hot, name: global_name, count: this.count}));
        this.$el.find('#' + this.count + ' .remove-button').on('click', this.remove_item);
        this.count++;

    },

    remove_item: function(event){
        var id = event.target.pa
      console.log(event);
    },

    show_list: function(){
        this.$el.find('#empty-message').hide();
        this.$el.find('#list-container').show();
    },

    hide_list: function(){

    }
});