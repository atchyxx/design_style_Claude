# Tab

元のフォルダ: `src/components/Tab/`。`scripts/add_components.py` で個別のファイルに展開できる。

<!-- file: Tab.tsx -->
````tsx
import { type ComponentProps, forwardRef } from 'react';

// Types

export type TabPosition = 'top' | 'bottom' | 'left' | 'right';

export type TabChangeDetail = {
  selectedIndex: number;
  selectedTabLabel: string;
};

// Tab (root wrapper)

export type TabProps = ComponentProps<'div'> & {
  position?: TabPosition;
};

export const Tab = ({ position = 'top', className, children, ...rest }: TabProps) => (
  <div
    className={`
      group/tab
      relative z-0 flex text-solid-gray-800 text-std-16N-170 [overflow-wrap:anywhere]
      data-[position=top]:flex-col data-[position=bottom]:flex-col
      data-[position=left]:flex-row data-[position=right]:flex-row-reverse
      ${className ?? ''}
    `}
    data-position={position}
    {...rest}
  >
    {children}
  </div>
);

// TabList

export type TabListProps = ComponentProps<'ul'>;

export const TabList = forwardRef<HTMLUListElement, TabListProps>(
  ({ className, children, ...rest }, ref) => (
    <ul
      ref={ref}
      className={`
        relative z-0 -m-1.5 overflow-hidden flex
        pt-[calc(7/16*1rem)] pr-1.5 pb-1.5 pl-[calc(7/16*1rem)]
        after:relative after:flex-grow after:border-0 after:border-solid after:border-solid-gray-420 after:content-['']
        group-data-[position=top]/tab:flex-wrap group-data-[position=top]/tab:after:-ml-px group-data-[position=top]/tab:after:w-px group-data-[position=top]/tab:after:border-b
        group-data-[position=bottom]/tab:flex-wrap-reverse group-data-[position=bottom]/tab:after:-mt-px group-data-[position=bottom]/tab:after:-ml-px group-data-[position=bottom]/tab:after:w-px group-data-[position=bottom]/tab:after:border-t
        group-data-[position=left]/tab:flex-col group-data-[position=left]/tab:shrink-0 group-data-[position=left]/tab:after:-mt-px group-data-[position=left]/tab:after:h-px group-data-[position=left]/tab:after:border-r
        group-data-[position=right]/tab:flex-col group-data-[position=right]/tab:shrink-0 group-data-[position=right]/tab:after:-mt-px group-data-[position=right]/tab:after:-ml-px group-data-[position=right]/tab:after:h-px group-data-[position=right]/tab:after:border-l
        ${className ?? ''}
      `}
      {...rest}
    >
      {children}
    </ul>
  ),
);

// TabItem

export type TabItemProps = ComponentProps<'a'> & {
  /**
   * @internal provided by useTabAria's getTabProps.
   * Applied to the inner <li> wrapper as role="presentation".
   */
  _internalListItemRole?: 'presentation';
  /**
   * @internal provided by useTabAria's getTabProps.
   * Renders the inner interactive element as <button> instead of <a>.
   */
  _internalElementType?: 'button';
};

export const TabItem = ({
  _internalListItemRole,
  _internalElementType,
  href,
  className,
  children,
  ...rest
}: TabItemProps) => {
  const computedClassName = `
    group/tab-item
    isolate -mt-px -ml-px flex border border-solid-gray-420 bg-white text-left no-underline
    [&[role=tab]]:cursor-default
    focus-visible:overflow-hidden focus-visible:z-[1]
    focus-visible:outline focus-visible:outline-4 focus-visible:outline-black
    focus-visible:outline-offset-[calc(2/16*1rem)] focus-visible:rounded-[calc(4/16*1rem)]
    focus-visible:ring-[calc(2/16*1rem)] focus-visible:ring-yellow-300
    [&:is([aria-selected=true],[aria-current]:not([aria-current='false'])):not(:focus-visible)]:before:absolute
    [&:is([aria-selected=true],[aria-current]:not([aria-current='false'])):not(:focus-visible)]:before:border-0
    [&:is([aria-selected=true],[aria-current]:not([aria-current='false'])):not(:focus-visible)]:before:border-solid
    [&:is([aria-selected=true],[aria-current]:not([aria-current='false'])):not(:focus-visible)]:before:border-white
    [&:is([aria-selected=true],[aria-current]:not([aria-current='false'])):not(:focus-visible)]:before:content-['']
    forced-colors:[&:is([aria-selected=true],[aria-current]:not([aria-current='false'])):not(:focus-visible)]:before:border-[Canvas]
    [&:not([aria-selected=true]):not([aria-current]:not([aria-current='false']))]:hover:bg-solid-gray-50
    group-data-[position=top]/tab:[&:is([aria-selected=true],[aria-current]:not([aria-current='false'])):not(:focus-visible)]:before:bottom-1.5
    group-data-[position=top]/tab:[&:is([aria-selected=true],[aria-current]:not([aria-current='false'])):not(:focus-visible)]:before:w-full
    group-data-[position=top]/tab:[&:is([aria-selected=true],[aria-current]:not([aria-current='false'])):not(:focus-visible)]:before:border-b
    group-data-[position=bottom]/tab:[&:is([aria-selected=true],[aria-current]:not([aria-current='false'])):not(:focus-visible)]:before:top-1.5
    group-data-[position=bottom]/tab:[&:is([aria-selected=true],[aria-current]:not([aria-current='false'])):not(:focus-visible)]:before:w-full
    group-data-[position=bottom]/tab:[&:is([aria-selected=true],[aria-current]:not([aria-current='false'])):not(:focus-visible)]:before:border-b
    group-data-[position=left]/tab:[&:is([aria-selected=true],[aria-current]:not([aria-current='false'])):not(:focus-visible)]:before:right-1.5
    group-data-[position=left]/tab:[&:is([aria-selected=true],[aria-current]:not([aria-current='false'])):not(:focus-visible)]:before:h-full
    group-data-[position=left]/tab:[&:is([aria-selected=true],[aria-current]:not([aria-current='false'])):not(:focus-visible)]:before:border-r
    group-data-[position=right]/tab:[&:is([aria-selected=true],[aria-current]:not([aria-current='false'])):not(:focus-visible)]:before:left-1.5
    group-data-[position=right]/tab:[&:is([aria-selected=true],[aria-current]:not([aria-current='false'])):not(:focus-visible)]:before:h-full
    group-data-[position=right]/tab:[&:is([aria-selected=true],[aria-current]:not([aria-current='false'])):not(:focus-visible)]:before:border-l
    ${className ?? ''}
  `;

  const inner = (
    <span
      className={`
        relative flex flex-grow items-center border-0 border-solid border-solid-gray-50
        p-4 font-normal text-dns-16N-120 [letter-spacing:0]
        group-aria-selected/tab-item:font-bold
        group-[&[aria-current]:not([aria-current='false'])]/tab-item:font-bold
        before:absolute before:content-['']
        group-aria-selected/tab-item:before:bg-key-900
        group-[&[aria-current]:not([aria-current='false'])]/tab-item:before:bg-key-900
        forced-colors:border-[Canvas]
        forced-colors:group-aria-selected/tab-item:before:bg-[ButtonText]
        forced-colors:group-[&[aria-current]:not([aria-current='false'])]/tab-item:before:bg-[ButtonText]
        group-[&:not([aria-selected=true]):not([aria-current]:not([aria-current='false'])):hover]/tab-item:underline
        group-[&:not([aria-selected=true]):not([aria-current]:not([aria-current='false'])):hover]/tab-item:underline-offset-[calc(3/16*1rem)]
        group-[&:not([aria-selected=true]):not([aria-current]:not([aria-current='false'])):hover]/tab-item:decoration-[calc(1/16*1rem)]
        group-[&:not([aria-selected=true]):not([aria-current]:not([aria-current='false'])):hover]/tab-item:before:bg-solid-gray-420
        group-data-[position=top]/tab:border-t-[5px] group-data-[position=top]/tab:before:-top-1.5 group-data-[position=top]/tab:before:left-0 group-data-[position=top]/tab:before:right-0 group-data-[position=top]/tab:before:h-1.5
        group-data-[position=bottom]/tab:border-b-[5px] group-data-[position=bottom]/tab:before:left-0 group-data-[position=bottom]/tab:before:-bottom-1.5 group-data-[position=bottom]/tab:before:right-0 group-data-[position=bottom]/tab:before:h-1.5
        group-data-[position=left]/tab:border-l-[5px] group-data-[position=left]/tab:before:top-0 group-data-[position=left]/tab:before:bottom-0 group-data-[position=left]/tab:before:-left-1.5 group-data-[position=left]/tab:before:w-1.5
        group-data-[position=right]/tab:border-r-[5px] group-data-[position=right]/tab:before:top-0 group-data-[position=right]/tab:before:-right-1.5 group-data-[position=right]/tab:before:bottom-0 group-data-[position=right]/tab:before:w-1.5
      `}
    >
      {children}
    </span>
  );

  return (
    <li role={_internalListItemRole} className='contents'>
      {_internalElementType === 'button' ? (
        <button type='button' className={computedClassName} {...(rest as ComponentProps<'button'>)}>
          {inner}
        </button>
      ) : (
        <a href={href} className={computedClassName} {...rest}>
          {inner}
        </a>
      )}
    </li>
  );
};

// TabPanel

export type TabPanelProps = ComponentProps<'div'>;

export const TabPanel = forwardRef<HTMLDivElement, TabPanelProps>(
  ({ className, children, ...rest }, ref) => (
    <div
      ref={ref}
      className={`
        border border-solid-gray-420 bg-white p-4
        focus-visible:z-[1] focus-visible:outline focus-visible:outline-4 focus-visible:outline-black
        focus-visible:outline-offset-[calc(2/16*1rem)] focus-visible:rounded-[calc(4/16*1rem)]
        focus-visible:ring-[calc(2/16*1rem)] focus-visible:ring-yellow-300
        group-data-[position=top]/tab:border-t-0
        group-data-[position=bottom]/tab:border-b-0
        group-data-[position=left]/tab:flex-grow group-data-[position=left]/tab:min-w-0 group-data-[position=left]/tab:border-l-0
        group-data-[position=right]/tab:flex-grow group-data-[position=right]/tab:min-w-0 group-data-[position=right]/tab:border-r-0
        ${className ?? ''}
      `}
      {...rest}
    >
      {children}
    </div>
  ),
);
````

<!-- file: index.ts -->
````ts
export * from './Tab';
export * from './useTab';
export * from './useTabAria';
````

<!-- file: useTab.ts -->
````ts
import { useEffect, useId, useRef, useState } from 'react';
import type { TabChangeDetail } from './Tab';

type UseTabOptions = {
  defaultSelectedIndex?: number;
  onTabChange?: (detail: TabChangeDetail) => void;
};

type TabGetListProps = {
  ref: React.RefObject<HTMLUListElement>;
  onClick: React.MouseEventHandler<HTMLUListElement>;
  onAuxClick: React.MouseEventHandler<HTMLUListElement>;
};

type TabGetTabProps = {
  href: string;
  'aria-current': true | undefined;
};

type TabGetPanelProps = {
  ref: (el: HTMLDivElement | null) => void;
  id: string;
  hidden: boolean;
};

export const useTab = ({ defaultSelectedIndex = 0, onTabChange }: UseTabOptions = {}) => {
  const [selectedIndex, setSelectedIndex] = useState(defaultSelectedIndex);
  const idBase = useId();
  const listRef = useRef<HTMLUListElement | null>(null);
  const panelRefs = useRef<(HTMLDivElement | null)[]>([]);
  const insertedHeadingsRef = useRef<HTMLElement[]>([]);
  const headingsInsertedRef = useRef(false);
  const headingIdBase = useId();

  // Track the index that should receive focus after the next render.
  const pendingFocusRef = useRef<number | null>(null);

  // Insert visually-hidden headings into each panel on mount.
  useEffect(() => {
    if (headingsInsertedRef.current) return;

    const list = listRef.current;
    if (!list) return;

    const labelledby = list.getAttribute('aria-labelledby');
    if (!labelledby) {
      console.warn('[useTab] aria-labelledby attribute is mandatory.');
      return;
    }

    const headingEl = document.getElementById(labelledby);
    const match = headingEl?.tagName.match(/^H([1-6])$/i);
    const parentLevel = match ? Number.parseInt(match[1], 10) : 2;
    const level = Math.min(parentLevel + 1, 6);

    const tabs = Array.from(list.querySelectorAll<HTMLAnchorElement>('a'));

    panelRefs.current.forEach((panel, index) => {
      if (!panel) return;
      const tab = tabs[index];
      if (!tab) return;

      const label = tab.textContent?.trim() ?? '';
      const heading = document.createElement(`h${level}`);
      heading.textContent = label;
      heading.id = `${headingIdBase}-panel-heading-${index}`;
      heading.setAttribute('tabindex', '-1');
      Object.assign(heading.style, {
        clip: 'rect(0 0 0 0)',
        clipPath: 'inset(50%)',
        height: '1px',
        overflow: 'hidden',
        position: 'absolute',
        whiteSpace: 'nowrap',
        width: '1px',
      });

      panel.insertBefore(heading, panel.firstChild);
      insertedHeadingsRef.current.push(heading);
    });

    headingsInsertedRef.current = true;

    return () => {
      for (const h of insertedHeadingsRef.current) {
        h.remove();
      }
      insertedHeadingsRef.current = [];
      headingsInsertedRef.current = false;
    };
  }, [headingIdBase]);

  // Focus the visually-hidden heading after the panel becomes visible.
  // biome-ignore lint/correctness/useExhaustiveDependencies: selectedIndex is an intentional trigger
  useEffect(() => {
    const index = pendingFocusRef.current;
    if (index === null) return;
    pendingFocusRef.current = null;
    insertedHeadingsRef.current[index]?.focus();
  }, [selectedIndex]);

  const getListProps = (): TabGetListProps => ({
    ref: listRef,
    onClick: (e) => {
      const target = (e.target as HTMLElement).closest('a');
      if (!target || !listRef.current?.contains(target)) return;

      e.preventDefault();

      const tabs = Array.from(listRef.current.querySelectorAll<HTMLAnchorElement>('a'));
      const index = tabs.indexOf(target);
      if (index === -1) return;

      setSelectedIndex(index);
      pendingFocusRef.current = index;

      if (onTabChange) {
        onTabChange({
          selectedIndex: index,
          selectedTabLabel: tabs[index]?.textContent?.trim() ?? '',
        });
      }
    },
    onAuxClick: (e) => {
      const target = (e.target as HTMLElement).closest('a');
      if (target && e.button === 1) e.preventDefault();
    },
  });

  const getTabProps = (index: number): TabGetTabProps => ({
    href: `#${idBase}-panel-${index}`,
    'aria-current': index === selectedIndex ? true : undefined,
  });

  const getPanelProps = (index: number): TabGetPanelProps => ({
    ref: (el) => {
      panelRefs.current[index] = el;
    },
    id: `${idBase}-panel-${index}`,
    hidden: index !== selectedIndex,
  });

  return { getListProps, getTabProps, getPanelProps };
};
````

<!-- file: useTabAria.ts -->
````ts
import { useId, useRef, useState } from 'react';
import type { TabChangeDetail } from './Tab';

type UseTabAriaOptions = {
  defaultSelectedIndex?: number;
  activation?: 'auto' | 'manual';
  onTabChange?: (detail: TabChangeDetail) => void;
};

type TabAriaGetListProps = {
  ref: React.RefObject<HTMLUListElement>;
  role: 'tablist';
  onClick: React.MouseEventHandler<HTMLUListElement>;
  onKeyDown: React.KeyboardEventHandler<HTMLUListElement>;
};

type TabAriaGetTabProps = {
  id: string;
  role: 'tab';
  'aria-selected': boolean;
  'aria-controls': string;
  tabIndex: 0 | -1;
  _internalListItemRole: 'presentation';
  _internalElementType: 'button';
};

type TabAriaGetPanelProps = {
  id: string;
  role: 'tabpanel';
  'aria-labelledby': string;
  tabIndex: 0;
  hidden: boolean;
};

export const useTabAria = ({
  defaultSelectedIndex = 0,
  activation = 'auto',
  onTabChange,
}: UseTabAriaOptions = {}) => {
  const [selectedIndex, setSelectedIndex] = useState(defaultSelectedIndex);
  const tablistRef = useRef<HTMLUListElement | null>(null);
  const idBase = useId();

  const selectTab = (index: number) => {
    setSelectedIndex(index);

    const list = tablistRef.current;
    const tabs = list ? Array.from(list.querySelectorAll<HTMLElement>('[role=tab]')) : [];
    tabs[index]?.focus();

    if (onTabChange) {
      onTabChange({
        selectedIndex: index,
        selectedTabLabel: tabs[index]?.textContent?.trim() ?? '',
      });
    }
  };

  const focusTab = (index: number) => {
    const list = tablistRef.current;
    const tabs = list ? Array.from(list.querySelectorAll<HTMLElement>('[role=tab]')) : [];
    tabs[index]?.focus();
  };

  const getListProps = (): TabAriaGetListProps => ({
    ref: tablistRef,
    role: 'tablist',
    onClick: (e) => {
      const target = (e.target as HTMLElement).closest<HTMLElement>('[role=tab]');
      if (!target || !tablistRef.current?.contains(target)) return;

      e.preventDefault();

      const tabs = Array.from(tablistRef.current.querySelectorAll<HTMLElement>('[role=tab]'));
      const index = tabs.indexOf(target);
      if (index === -1) return;

      selectTab(index);
    },
    onKeyDown: (e) => {
      const target = (e.target as HTMLElement).closest<HTMLElement>('[role=tab]');
      if (!target || !tablistRef.current?.contains(target)) return;

      const tabs = Array.from(tablistRef.current.querySelectorAll<HTMLElement>('[role=tab]'));
      const currentIndex = tabs.indexOf(target);
      const count = tabs.length;
      const isManual = activation === 'manual';

      const activate = isManual ? (i: number) => focusTab(i) : (i: number) => selectTab(i);

      switch (e.key) {
        case 'ArrowLeft':
        case 'ArrowUp':
          e.preventDefault();
          if (currentIndex > 0) activate(currentIndex - 1);
          break;
        case 'ArrowRight':
        case 'ArrowDown':
          e.preventDefault();
          if (currentIndex < count - 1) activate(currentIndex + 1);
          break;
        case 'Home':
          e.preventDefault();
          activate(0);
          break;
        case 'End':
          e.preventDefault();
          activate(count - 1);
          break;
      }
    },
  });

  const getTabProps = (index: number): TabAriaGetTabProps => ({
    id: `${idBase}-tab-${index}`,
    role: 'tab',
    'aria-selected': index === selectedIndex,
    'aria-controls': `${idBase}-panel-${index}`,
    tabIndex: index === selectedIndex ? 0 : -1,
    _internalListItemRole: 'presentation',
    _internalElementType: 'button',
  });

  const getPanelProps = (index: number): TabAriaGetPanelProps => ({
    id: `${idBase}-panel-${index}`,
    role: 'tabpanel',
    'aria-labelledby': `${idBase}-tab-${index}`,
    tabIndex: 0,
    hidden: index !== selectedIndex,
  });

  return { getListProps, getTabProps, getPanelProps };
};
````
