from django.views import generic
from django.contrib.auth.decorators import permission_required


class RestrictedListView(generic.ListView):
    """ Generic list view that checks permissions """
    def dispatch(self, request, *args, **kwargs):
        perm = '%s.change_%s' % (self.model._meta.app_label, self.model._meta.model_name)
        @permission_required(perm, raise_exception=True)
        def wrapper(request, *args, **kwargs):
            return super(RestrictedListView, self).dispatch(request, *args, **kwargs)
        return wrapper(request, *args, **kwargs)


class RestrictedUpdateView(generic.UpdateView):
    """ Generic update view that checks permissions """
    def dispatch(self, request, *args, **kwargs):
        perm = '%s.change_%s' % (self.model._meta.app_label, self.model._meta.model_name)
        @permission_required(perm, raise_exception=True)
        def wrapper(request, *args, **kwargs):
            return super(RestrictedUpdateView, self).dispatch(request, *args, **kwargs)
        return wrapper(request, *args, **kwargs)


class RestrictedCreateView(generic.CreateView):
    """ Generic create view that checks permissions """
    def dispatch(self, request, *args, **kwargs):
        perm = '%s.add_%s' % (self.model._meta.app_label, self.model._meta.model_name)
        @permission_required(perm, raise_exception=True)
        def wrapper(request, *args, **kwargs):
            return super(RestrictedCreateView, self).dispatch(request, *args, **kwargs)
        return wrapper(request, *args, **kwargs)


class RestrictedDeleteView(generic.DeleteView):
    """ Generic delete view that checks permissions """
    def dispatch(self, request, *args, **kwargs):
        perm = '%s.delete_%s' % (self.model._meta.app_label, self.model._meta.model_name)
        @permission_required(perm, raise_exception=True)
        def wrapper(request, *args, **kwargs):
            return super(RestrictedDeleteView, self).dispatch(request, *args, **kwargs)
        return wrapper(request, *args, **kwargs)
