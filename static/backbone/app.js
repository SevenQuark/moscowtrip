

var SideBarView = Backbone.View.extend({

    initialize: function(){
        this.empty = true;
        this.render();
    },

    render: function(){

        var template = _.template($('#sidebar-template').html())
        this.$el.html(template({empty: this.empty}));
        return this;

    },

    add_event: function(global_hot, global_name, date){
        if( this.empty){
            this.empty = false;
            this.show_list();
        }
        this.$el.find('#' + date).append('<div class="event-item">' +
                                        '<a href="#"><i class="glyphicon glyphicon-remove-circle" style="color:#d2554f"></i></a>' +
                                        '<span class="text-success">Some relax event</span></div>');


    },

    show_list: function(){
        this.$el.find('#empty-message').hide();
        this.$el.find('#list-container').show();
    },

    hide_list: function(){

    }
});