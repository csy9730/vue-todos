# comments
## arch

- index.html
- src/main.js
	- src/App.vue  {router-view} `<router-view></router-view>`
	- src/router/index.js {layouts, todo}
	- src/components/layouts.vue {menus, todo}  `<menus></menus>  <router-view></router-view>` ,与store 数据交互 menuOpen
	- src/components/menus.vue {item}, 菜单栏包含item列表，[{标题，数量， 锁定标记}]
    	- item 来自 `this.$store.getters.getTodoList`
	- src/components/todo.vue {item} 包含 [标题栏，输入栏， item列表]
    	- `<item ></item>`
    	- {id, title, count, isDelete, locked, record(items):[item{}]}
	- src/components/item.vue 代办单项组件  {text, checked, isDelete}
- src/vuex/store.js


export default 可以理解成匿名导出？
#### src/router/index.js
``` js
import todo from '@/components/todo';
export default new Router({
  routes: [{
    path: '/',
    name: 'Hello',
    component: layouts,
    children: [{
      path: '/todo/:id',
      name: 'todo',
      component: todo
    }]
  }]
});
```
## main

- npm install --legacy-peer-deps
- npm run dev

## misc

### todo
- [ ] src/vuex/store.js
- [x] node run dev

