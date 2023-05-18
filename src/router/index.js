import Vue from 'vue';
import Router from 'vue-router';
import TodoView from '@/views/TodoView';
import NotFound from '@/views/NotFound';
import HomeView from '@/views/HomeView';
import todo from '@/components/todo';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/todo',
      name: 'todos',
      component: TodoView,
      children: [{
        path: '/todo/:id',
        name: 'todo',
        component: todo
      }]
    },
    {
      path: '/demo',
      // name: 'about',
      component: () => import('../views/DemoView.vue')
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'NotFound',
      component: NotFound
    }
  ]
});
