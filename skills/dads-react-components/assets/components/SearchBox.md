# SearchBox

元のフォルダ: `src/components/SearchBox/`。`scripts/add_components.py` で個別のファイルに展開できる。

<!-- file: SearchBox.tsx -->
````tsx
import { type ComponentProps, forwardRef } from 'react';
import { Button, type ButtonProps } from '../Button';

export type SearchBoxSize = 'lg' | 'md' | 'sm';

export type SearchBoxProps = ComponentProps<'div'> & {
  size?: SearchBoxSize;
};

export const SearchBox = forwardRef<HTMLDivElement, SearchBoxProps>((props, ref) => {
  const { children, className, size = 'lg', ...rest } = props;

  return (
    <div
      className={`
        group/search-box
        grid [grid-template-areas:'fields_submit'_'detail_detail'] grid-cols-[1fr_auto] gap-x-4
        text-solid-gray-900 text-oln-16N-100 font-sans
        ${className ?? ''}
      `}
      data-size={size}
      ref={ref}
      {...rest}
    >
      {children}
    </div>
  );
});

export type SearchBoxFieldsProps = ComponentProps<'div'>;

export const SearchBoxFields = forwardRef<HTMLDivElement, SearchBoxFieldsProps>((props, ref) => {
  const { children, className, ...rest } = props;

  return (
    <div className={`relative z-0 flex [grid-area:fields] ${className ?? ''}`} ref={ref} {...rest}>
      {children}
    </div>
  );
});

export type SearchBoxSelectProps = ComponentProps<'select'> & {
  label: string;
};

export const SearchBoxSelect = forwardRef<HTMLSelectElement, SearchBoxSelectProps>((props, ref) => {
  const { children, className, label, ...rest } = props;

  return (
    <label className='dads-search-box__select relative flex shrink-0'>
      <span
        className={`
          absolute top-[calc(50%-1.25rem)] left-[calc(17/16*1rem)] z-[2] text-solid-gray-700 pointer-events-none
          group-data-[size=sm]/search-box:sr-only
          group-data-[size=md]/search-box:top-[calc(50%-1.125rem)]
        `}
      >
        {label}
      </span>
      <select
        className={`
          appearance-none flex items-center overflow-hidden
          w-40 rounded-l-8 rounded-r-none
          border border-solid-gray-600
          bg-solid-gray-50
          pt-5 pr-10 pb-0 pl-4
          text-solid-gray-900 text-oln-17N-100 font-sans
          whitespace-nowrap text-ellipsis
          hover:border-black
          focus-visible:relative focus-visible:z-[1]
          focus-visible:outline focus-visible:outline-4 focus-visible:outline-black
          focus-visible:outline-offset-[calc(2/16*1rem)] focus-visible:ring-[calc(2/16*1rem)] focus-visible:ring-yellow-300
          group-data-[size=md]/search-box:pt-[calc(18/16*1rem)]
          group-data-[size=sm]/search-box:pt-0
          ${className ?? ''}
        `}
        ref={ref}
        {...rest}
      >
        {children}
      </select>
      <svg
        aria-hidden={true}
        className='pointer-events-none absolute right-4 top-0 bottom-0 my-auto z-[1] w-4 h-4'
        width='16'
        height='16'
        viewBox='0 0 24 24'
      >
        <path d='M12 17L3 8L4 7L12 15L20 7L21 8L12 17Z' fill='currentColor' />
      </svg>
    </label>
  );
});

export type SearchBoxInputProps = Omit<ComponentProps<'input'>, 'aria-labelledby'> &
  ({ label: string; 'aria-labelledby'?: never } | { label?: never; 'aria-labelledby': string });

export const SearchBoxInput = forwardRef<HTMLInputElement, SearchBoxInputProps>((props, ref) => {
  const { className, label, ...rest } = props;

  return (
    <label className='relative flex grow'>
      <svg
        aria-hidden={true}
        className='pointer-events-none absolute left-4 top-0 bottom-0 my-auto z-[1] w-6 h-6 text-solid-gray-600 forced-colors:text-[CanvasText]'
        width='24'
        height='24'
        viewBox='0 0 24 24'
      >
        <path
          d='m21 20.5-6-6a7.4 7.4 0 0 0 1.9-5A7.4 7.4 0 0 0 9.5 2 7.5 7.5 0 1 0 14 15.5l6 6 1-1ZM3.5 9.5a6 6 0 0 1 6-6 6 6 0 0 1 6 6 6 6 0 0 1-6 6 6 6 0 0 1-6-6Z'
          fill='currentColor'
        />
      </svg>
      {label !== undefined && <span className='sr-only'>{label}</span>}
      <input
        className={`
          grow w-32
          border border-solid-gray-600 rounded-8 bg-white
          pt-3 pr-4 pb-3 pl-12
          placeholder:text-solid-gray-600
          hover:border-black
          focus-visible:relative
          focus-visible:outline focus-visible:outline-4 focus-visible:outline-black
          focus-visible:outline-offset-[calc(2/16*1rem)] focus-visible:ring-[calc(2/16*1rem)] focus-visible:ring-yellow-300
          group-data-[size=md]/search-box:pt-[calc(11/16*1rem)] group-data-[size=md]/search-box:pb-[calc(11/16*1rem)]
          group-data-[size=sm]/search-box:pt-[calc(7/16*1rem)] group-data-[size=sm]/search-box:pb-[calc(7/16*1rem)]
          [label:not(:first-child)_&]:-ml-px [label:not(:first-child)_&]:rounded-tl-none [label:not(:first-child)_&]:rounded-bl-none
          [&::-webkit-search-cancel-button]:hidden
          ${className ?? ''}
        `}
        ref={ref}
        {...rest}
      />
    </label>
  );
});

export type SearchBoxDetailProps = ComponentProps<'details'> & {
  summary: string;
};

export const SearchBoxDetail = forwardRef<HTMLDetailsElement, SearchBoxDetailProps>(
  (props, ref) => {
    const { children, className, summary, ...rest } = props;

    return (
      <details
        className={`
          group/disclosure
          mt-4 [grid-area:detail] w-fit border border-solid-gray-600 rounded-8 py-3 px-4
          text-solid-gray-800 text-std-16N-170 font-sans
          open:w-auto open:pb-6
          ${className ?? ''}
        `}
        ref={ref}
        {...rest}
      >
        <summary
          className={`
            group/summary
            flex items-start justify-start gap-2 w-fit cursor-default list-none
            -mx-4 -my-3 px-4 py-3
            [&::-webkit-details-marker]:hidden [&::marker]:content-['']
            hover:underline hover:underline-offset-[calc(3/16*1rem)]
            focus-visible:outline focus-visible:outline-4 focus-visible:outline-black
            focus-visible:outline-offset-[calc(2/16*1rem)] focus-visible:rounded-4
            focus-visible:bg-yellow-300 focus-visible:ring-[calc(2/16*1rem)] focus-visible:ring-yellow-300
          `}
        >
          <svg
            aria-hidden={true}
            className='shrink-0 mt-[calc((1lh-24px)/2)] text-key-1000 forced-colors:text-inherit group-open/disclosure:rotate-180'
            width='24'
            height='24'
            viewBox='0 0 24 24'
          >
            <circle cx='12' cy='12' r='11' fill='currentColor' />
            <circle
              className='group-hover/summary:fill-[Canvas]'
              cx='12'
              cy='12'
              r='8'
              fill='currentColor'
            />
            <path
              className='group-hover/summary:fill-current'
              d='M17 10H7L12 15L17 10Z'
              fill='Canvas'
            />
          </svg>
          {summary}
        </summary>
        <div className='mt-8'>{children}</div>
      </details>
    );
  },
);

export type SearchBoxDetailActionsProps = ComponentProps<'div'>;

export const SearchBoxDetailActions = forwardRef<HTMLDivElement, SearchBoxDetailActionsProps>(
  (props, ref) => {
    const { children, className, ...rest } = props;

    return (
      <div className={`flex flex-col items-center gap-4 ${className ?? ''}`} ref={ref} {...rest}>
        {children}
      </div>
    );
  },
);

export type SearchBoxSubmitProps = ButtonProps;

export const SearchBoxSubmit = forwardRef<HTMLButtonElement, SearchBoxSubmitProps>((props, ref) => {
  const { className, variant, ...rest } = props;

  return (
    <Button
      className={`
          [grid-area:submit] cursor-pointer
          group-has-[details[open]]/search-box:invisible
          ${className ?? ''}
        `}
      variant={variant ?? 'solid-fill'}
      ref={ref}
      {...(rest as ButtonProps)}
    />
  );
});
````

<!-- file: index.ts -->
````ts
export * from './SearchBox';
````

<!-- file: search-box.css -->
````css
@supports (appearance: base-select) {
  .dads-search-box__select > select {
    appearance: base-select;
  }

  .dads-search-box__select > select::picker-icon {
    display: none;
  }

  .dads-search-box__select > select::picker(select) {
    appearance: base-select;
    border: 1px solid #949494; /* solid-gray-420 */
    box-shadow:
      0 2px 8px 1px rgba(0, 0, 0, 0.1),
      0 1px 5px 0 rgba(0, 0, 0, 0.3); /* shadow-1 */
    padding: calc(16 / 16 * 1rem) 0;
  }
}

.dads-search-box__select option {
  display: flex;
  align-items: center;
  box-sizing: border-box;
  min-height: calc(44 / 16 * 1rem);
  padding: calc(10 / 16 * 1rem) calc(16 / 16 * 1rem);
  color: #1a1a1a; /* solid-gray-900 */
}

.dads-search-box__select option::checkmark {
  display: none;
}

@media (hover: hover) {
  .dads-search-box__select option:hover {
    background-color: #f2f2f2; /* solid-gray-50 */
    text-decoration: underline;
    text-decoration-thickness: calc(1 / 16 * 1rem);
    text-underline-offset: calc(3 / 16 * 1rem);
  }
}

.dads-search-box__select option:checked {
  font-weight: bold;
  background-color: #d9e6ff; /* key-100 */
  color: #00118f; /* key-1000 */
}

@media (hover: hover) {
  .dads-search-box__select option:checked:hover {
    background-color: #e8f1fe; /* key-50 */
    color: #0017c1; /* key-900 */
  }
}

.dads-search-box__select option:focus-visible {
  border-radius: 0;
  outline: calc(4 / 16 * 1rem) solid #000000;
  outline-offset: calc(-4 / 16 * 1rem);
  box-shadow: none;
}

.dads-search-box__select option:not(:checked):focus-visible {
  background-color: #ffd43d; /* yellow-300 */
}

.dads-search-box__select option:checked:focus-visible {
  box-shadow: inset 0 0 0 calc(6 / 16 * 1rem) #ffd43d; /* yellow-300 */
}
````
