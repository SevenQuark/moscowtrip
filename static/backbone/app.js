

var SideBarView = Backbone.View.extend({

    initialize: function(){
        this.empty = true;
        this.render();
    },

    render: function(){

        var template = _.template($('#sidebar-template').html())
        this.$el.html(template({empty: this.empty}));
        return this;

    }
});